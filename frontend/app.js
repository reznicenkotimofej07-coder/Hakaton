let recorder;
let chunks = [];
let stream;

const startButton = document.querySelector("#start");
const stopButton = document.querySelector("#stop");
const statusText = document.querySelector("#status");

startButton.onclick = async () => {
    try {
        stream = await navigator.mediaDevices.getUserMedia({
            audio: true
        });

        recorder = new MediaRecorder(stream);
        chunks = [];

        recorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                chunks.push(event.data);
            }
        };

        recorder.onstop = async () => {
            stream.getTracks().forEach(track => track.stop());

            const blob = new Blob(chunks, {
                type: recorder.mimeType
            });

            await uploadAudio(blob);
        };

        recorder.start();

        startButton.disabled = true;
        stopButton.disabled = false;
        statusText.textContent = "Идёт запись...";

    } catch (error) {
        statusText.textContent = "Ошибка микрофона";
        console.error(error);
    }
};

stopButton.onclick = () => {
    recorder.stop();

    startButton.disabled = false;
    stopButton.disabled = true;
};

async function uploadAudio(blob) {
    const formData = new FormData();

    const extension = blob.type.includes("ogg")
        ? "ogg"
        : blob.type.includes("mp4")
        ? "m4a"
        : "webm";

    formData.append("file", blob, `audio.${extension}`);

    statusText.textContent = "Отправка аудио...";

    try {
        const response = await fetch("/api/audio/upload", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const result = await response.json();

        statusText.textContent = "Аудио отправлено";
        console.log(result);

    } catch (error) {
        statusText.textContent = "Ошибка отправки";
        console.error(error);
    }
}