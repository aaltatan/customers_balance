<script>
  import { onMount } from 'svelte';
  import { Link } from 'svelte-routing';

  onMount(() => {
    document.title = 'Not Found';
  })

</script>

<div class="flex items-center justify-center flex-col gap-4">
  <h1 class="text-7xl font-bold tracking-tighter">
    Oops!
  </h1>
  <p class="font-semibold">404 - Page not found</p>
  <p class="text-slate-500 tracking-tighter">we could not found the page you are looking for</p>
  <Link to="/" class="btn btn-primary py-2 px-4">
    go to Homepage
  </Link>
</div>