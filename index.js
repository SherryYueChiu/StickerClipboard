/**
 * 單一貼圖資料
 * @typedef {Object} OneStickerData
 * @property {string} name
 * @property {string} type
 *//**
* 貼圖包資料
* @typedef {Object} StickerPackData
* @property {string} name
* @property {string} type
* @property {OneStickerData[]} children
*/

/** 
 * 貼圖資料
 * @type {StickerPackData[]} 
 */
var fileTree = {};

// register service worker
navigator.serviceWorker.register('service-worker.js', { scope: "." });

// request permission
CopyImageClipboard.requestClipboardWritePermission();

// load data
fetch('./stickerFileTree.json')
    .then((response) => response.json())
    .then((json) => {
        fileTree = json.children;
        showStickerPackList();
    });

function showStickerPackList() {
    console.log('showStickerPackList');
    fileTree.forEach((pack, i) => {
        let thumbnailSticker = pack.children[0];
        let imgElm = document.createElement('img');
        imgElm.name = pack.name;
        imgElm.index = i;
        imgElm.classList.add('sticker-preview');
        imgElm.src = `./allSticker/${pack.name}/${thumbnailSticker.name}`;
        imgElm.setAttribute('onclick', `showStickersInPack(${i})`);
        document.querySelector('.stickerPackList').append(imgElm);
        updateHeaderTitle('貼圖剪貼簿');
    });
}

function showStickersInPack(packIndex) {
    console.log('showStickersInPack', packIndex);
    const $stickerPackList = document.querySelector('.stickerPackList');
    const $stickerList = document.querySelector('.stickerList');
    $stickerList.innerHTML = '';
    fileTree[packIndex].children.forEach((sticker, i) => {
        let imgElm = document.createElement('img');
        imgElm.name = sticker.name;
        imgElm.setAttribute('index', i);
        imgElm.classList.add('sticker-normal');
        imgElm.src = `./allSticker/${fileTree[packIndex].name}/${sticker.name}`;
        imgElm.setAttribute('onclick', `copyStickerImage(${packIndex},${i})`);
        $stickerList.append(imgElm);
    });
    $stickerPackList.classList.add('hide');
    $stickerList.classList.remove('hide');
    toggleBackBottom(true);
    updateHeaderTitle(fileTree[packIndex].name);
}

function backToStickerPackList() {
    const $stickerPackList = document.querySelector('.stickerPackList');
    const $stickerList = document.querySelector('.stickerList');
    $stickerPackList.classList.remove('hide');
    $stickerList.classList.add('hide');
    toggleBackBottom(false);
}

function updateHeaderTitle(title) {
    const $title = document.querySelector('.header>.title');
    $title.innerHTML = title;
}

function copyStickerImage(packIdx, stickerIdx) {
    CopyImageClipboard.copyImageToClipboard(`./allSticker/${fileTree[packIdx].name}/${fileTree[packIdx].children[stickerIdx].name}`)
        .then(() => {
            console.log('Image Copied');
        })
        .catch((e) => {
            console.log('Error: ', e.message);
        });
}

function toggleBackBottom(show) {
    const $backBtn = document.querySelector('.header>.back');
    if (show) $backBtn.classList.remove('hide');
    else $backBtn.classList.add('hide');
}