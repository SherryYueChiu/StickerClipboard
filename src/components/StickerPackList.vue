<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import * as _stickerDataLib from "../stickerFileTree.json";
import { StickerPackData, StickerDataLib } from "../type.ts";
import { packImageReloadTimer, selectedPack } from "../store.ts";

const router = useRouter();
const stickerDataLib: StickerDataLib = (_stickerDataLib as any)
  ?.default as StickerDataLib;

onMounted(() => {
  // 10秒自動重播
  clearInterval(packImageReloadTimer.value);
  packImageReloadTimer.value = setInterval(reloadGifs, 10000);
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

function launchStickerPack(stickerPack: StickerPackData) {
  selectedPack.value = stickerPack;
  router.push({ name: "StickerList", query: { view: "StickerList" } });
}
</script>

<template>
  <div class="container">
    <div class="header">
      <div class="title">貼圖剪貼簿</div>
    </div>
    <div class="stickerPackList">
      <img
        class="stickerPreview"
        v-for="stickerPack in stickerDataLib.children"
        :src="`/allSticker/${stickerPack.name}/${stickerPack.children[0].name}`"
        @click="launchStickerPack(stickerPack)"
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
      font-size: 1.2rem;
    }
  }
  & > .title {
    display: block;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.5rem;
    font-weight: 700;
    color: aliceblue;
  }
}
.container {
  display: block;
  position: relative;
  height: 100vh;
  overflow-y: auto;
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
</style>
