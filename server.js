const WebSocket = require('ws');
const fs = require('fs');
const readline = require('readline');

const wss = new WebSocket.Server({ port: 8080 });

const clients = new Map();
let currentId = 1;

const frames = fs.readFileSync('./frames.txt', 'utf-8').split('&');

let currentFrameIndex = 0;
let isPlaying = false;

wss.on('connection', (ws) => {
    const id = currentId++;
    clients.set(id, ws);

    console.log(`Client ${id} connected`);

    ws.send(JSON.stringify({ type: 'id', id }));

    ws.on('close', () => {
        clients.delete(id);
        console.log(`Client ${id} disconnected`);
    });
});

const playFrames = () => {
    if (!isPlaying) {
        currentFrameIndex = 0;
        return;
    }
    const frame = frames[currentFrameIndex];
    if (!frame) return;

    const rows = frame.split('\n');
    console.log(`Playing frame ${currentFrameIndex}`);

    clients.forEach((ws, id) => {
        const binaryCode = rows[id % rows.length];
        const value = binaryCode[id % binaryCode.length];
        const state = parseInt(value, 10);
        ws.send(JSON.stringify({ type: 'state', state }));
    });

    currentFrameIndex = currentFrameIndex + 1;
};

setInterval(playFrames, 50);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on('line', (input) => {
    if (input.trim().toLowerCase() === '1') {
        isPlaying = true;
        console.log('开始播放');
    } else if (input.trim().toLowerCase() === '0') {
        isPlaying = false;
        console.log('暂停播放');
    }
});

console.log('WebSocket server is running on ws://localhost:8080');
console.log('在标签页全部打开后，输入 1 开始播放，输入 0 暂停播放');