<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import { copyImageToClipboard } from "copy-image-clipboard";
import * as _stickerDataLib from "../stickerFileTree.json";
import { stickerImageReloadTimer, selectedPack } from "../store.ts";
import { StickerPackData, OneStickerData } from "../type.ts";

const router = useRouter();

if (!selectedPack.value) {
  router.replace({
    name: "StickerPackList",
    query: { view: "StickerPackList" },
  });
}

onMounted(() => {
  // 10秒自動重播
  clearInterval(stickerImageReloadTimer.value);
  stickerImageReloadTimer.value = setInterval(reloadGifs, 10000);
});

function reloadGifs() {
  document.querySelectorAll("img").forEach((img) => {
    const src = img.src;
    img.removeAttribute("src");
    // setTimeout(() => {
    img.src = src;
    // }, 20);
  });
}

function routerBack() {
  router.go(-1);
}

function conclickSticker(pack: StickerPackData, sticker: OneStickerData) {
  copyImageToClipboard(`/allSticker/${pack.name}/${sticker.name}`)
    .then(() => {
      console.log("Image Copied");
    })
    .catch((e) => {
      console.log("Error: ", e.message);
    });
}
</script>

<template>
  <div class="container">
    <div class="header">
      <div class="back hide" @click="routerBack">
        <a>返回</a>
      </div>
      <div class="title">{{ selectedPack?.name }}</div>
    </div>
    <div class="stickerPackList">
      <img
        class="stickerPreview"
        v-for="sticker in selectedPack?.children"
        :src="`/allSticker/${selectedPack.name}/${sticker.name}`"
        @click="conclickSticker(selectedPack, sticker)"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.header {
  display: block;
  position: fixed;
  width: 100%;
  height: 4rem;
  background: brown;
  & > .back {
    display: block;
    position: absolute;
    width: 5rem;
    height: 3rem;
    border-radius: 0.5rem;
    background: bisque;
    left: 0.5rem;
    top: 0.5rem;
    & > * {
      display: block;
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      color: brown;
      font-weight: 600;
      font-size: 1.1rem;
    }
  }
  & > .title {
    display: block;
    position: absolute;
    width: calc(100% - 6rem);
    left: calc(50% + 3rem);
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.5rem;
    font-weight: 700;
    color: aliceblue;
    text-align: center;
  }
}
.container {
  display: block;
  position: relative;
  height: 100vh;
  overflow-y: auto;
  background: #fff;
  animation: grayscaleBackground 10s infinite;
}
.stickerPackList {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 5rem 0 2rem 0;
}

.stickerPreview {
  width: 25%;
  max-width: 150px;
  height: auto;
}
@keyframes grayscaleBackground {
  0% {
    background: #fff;
  }
  50% {
    background: #000;
  }
  100% {
    background: #fff;
  }
}
</style>
