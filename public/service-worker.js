const CACHE_NAME = 'sticker-clipboard-v1';
const urlsToCache = [
  './',
  './**/*'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Clone the response as it can only be consumed once
        const responseToCache = response.clone();
        
        // Open the cache and store the response
        caches.open(CACHE_NAME)
          .then(cache => {
            cache.put(event.request, responseToCache);
          });
        
        return response;
      })
      .catch(() => {
        // If network fails, try to get from cache
        return caches.match(event.request)
          .then(cachedResponse => {
            if (cachedResponse) {
              return cachedResponse;
            }
            // If not in cache, return a fallback response
            return new Response('Network error occurred');
          });
      })
  );
});
