import { createRouter, createWebHistory } from 'vue-router';
import StickerPackList from './components/StickerPackList.vue';
import StickerList from './components/StickerList.vue';

const routes = [
  {
    path: '/',
    name: 'StickerPackList',
    component: StickerPackList,
    beforeEnter: (to, _, next) => {
      if (to.query.view === 'StickerList') {
        next({ name: 'StickerList', query: to.query });
      } else {
        next();
      }
    }
  },
  {
    path: '/',
    name: 'StickerList',
    component: StickerList,
    props: true
  },
];


const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;