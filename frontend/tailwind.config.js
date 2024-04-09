/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './public/index.html',
    './src/*.svelte',
    './src/**/*.svelte',
    './src/**/**/*.svelte',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

