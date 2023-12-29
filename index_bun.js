const server = Bun.serve({
  port: 8083,
  fetch(req) {
    return new Response("Hello World!\n");
  },
});
