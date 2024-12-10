import { StickerPackData } from './type.ts';
import { ref } from 'vue';

export const selectedPack = ref<StickerPackData>();
export const packImageReloadTimer = ref<any>();
export const stickerImageReloadTimer = ref<any>();