<script setup lang="ts">
import { ref, onMounted } from "vue";

</script>
<template>
  <header  class="align-items-center header-container">
    <img id="logo-img" class="responsive-small-image mr-2 ml-2" src="/logo.webp" alt="logo">
   <div class="col menu">
    <RouterLink to="/">Home</RouterLink>
    <RouterLink to="/order">Menu</RouterLink>
    <RouterLink to="/cart">Carrinho</RouterLink>
   </div>
    <button class="mr-2 ml-2 custom-button-light up-element">
      <i class="pi pi-sign-in mr-2"></i>
      <RouterLink to="/login">Entrar</RouterLink>
    </button>
  </header>
</template>


<style scoped lang="scss">
.header-container {
  display: flex;
  height: var(--app-header-height);
  

  
  .menu {
    border: none;
    position: relative;
    z-index: 2;

    
    .router-link-exact-active{
      font-weight: bold
    }
  }

  #logo-img {
    display: none;
  }
}


@media (min-width: 500px) {
  .header-container{    
  button{
    position: relative;
    z-index: 2;
  }

  .menu{
    background-color: var(--app-background);
    z-index: 0;
    a{
      padding: 1rem;
    }
  }

    #logo-img {
      display: block;
    }
  }
}
</style>