import App from './App.svelte';
import './locale/i18n';

const app = new App({
	target: document.querySelector('#app'),
});

export default app;