<script>
  export let endpoint = '/api/customers/excel';
  
  import Loading  from './icons/Loading.svelte'
  import { _ } from 'svelte-i18n';

  let loading = false;

  const exportHandler = async () => {
    loading = true;
    const response = await fetch(endpoint);
    const blob = await response.blob();

    const url = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.style.display = 'none';
    link.href = url;

    document.body.appendChild(link);
    link.click();
    URL.revokeObjectURL(url);
    link.remove();
    loading = false;
  }
</script>

<button
  on:click={exportHandler}
  class="btn btn-success !flex items-center gap-1 py-2 px-3"
>
  {#if loading}
    <Loading ratio="1.5rem"/>
  {/if}
  <span>{$_('buttons.exportExcel')}</span>
</button>