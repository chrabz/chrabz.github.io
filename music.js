const musicList = document.getElementById("music-list");

musicFiles.forEach(file => {
    let fileName = file.split("/").pop().replace(".mp3", "");

    let musicItem = document.createElement("div");
    musicItem.classList.add("music-item");

    let title = document.createElement("p");
    title.textContent = fileName;

    let audio = document.createElement("audio");
    audio.controls = true;
    audio.src = "music/" + file;

    musicItem.appendChild(title);
    musicItem.appendChild(audio);
    musicList.appendChild(musicItem);
});