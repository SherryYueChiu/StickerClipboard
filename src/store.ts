import { StickerPackData } from './type.ts';
import { ref } from 'vue';

export const selectedPack = ref<StickerPackData>();
export const packImageReloadTimer = ref<NodeJS.Timeout>();
export const stickerImageReloadTimer = ref<NodeJS.Timeout>();