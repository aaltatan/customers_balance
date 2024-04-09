<script>
  import { Router, Route } from "svelte-routing";
  import Header from "./components/Header.svelte";
  import HomePage from "./pages/HomePage.svelte";
  import Transactions from "./pages/Transactions.svelte";
  import Add from "./pages/Add.svelte";
  import Ledger from "./pages/Ledger.svelte";
  import NotFound from "./pages/NotFound.svelte";
  import { setContext } from 'svelte'

  setContext('username', localStorage.getItem('username'))

  export let url = "";
</script>

<Router {url}>
  <div class="w-[min(90%,80ch)] my-2 md:my-8 mx-auto">
    <Header />
    <main class="pt-8 pb-20">
      <Route path="/"><HomePage /></Route>
      <Route path="/home"><HomePage /></Route>
      <Route path="/transactions" component={Transactions} />
      <Route path="/add/">
        <Add type="debit" />
      </Route>
      <Route path="/add-debit/:id" let:params>
        <Add id={params.id} type="debit" />
      </Route>
      <Route path="/add-credit/:id" let:params>
        <Add id={params.id} type="credit" />
      </Route>
      <Route path="/ledger/:id" let:params>
        <Ledger id={params.id} />
      </Route>
      <Route path="/*" component={NotFound} />
    </main>
  </div>
</Router>
