import { init, addMessages } from "svelte-i18n";
import ar from './ar';
import en from './en';

addMessages('en', en)
addMessages('ar', ar)

init({
	fallbackLocale: localStorage.getItem('lang') || 'ar',
});