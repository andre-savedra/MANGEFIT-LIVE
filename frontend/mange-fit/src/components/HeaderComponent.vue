<script setup lang="ts">
import { ref } from "vue";
const items = ref([
  {
    label: 'TESTE',
    icon: 'pi pi-home'
  },
  {
    label: 'Menu',
    icon: 'pi pi-shopping-bag',    
  },
  {
    label: 'Carrinho',
    icon: 'pi pi-shopping-cart'
  }
]);

</script>
<template>
  <header class="align-items-center header-container">
    <img id="logo-img" class="responsive-small-image mr-2 ml-2" src="/logo.webp" alt="logo">
    <Menubar :model="items" class="col menu" />
    <button class="mr-2 ml-2 custom-button-light">
      <i class="pi pi-sign-in mr-2"></i>
      Entrar
    </button>
  </header>
</template>


<style scoped lang="scss">
.header-container {
  display: flex;
  height: var(--app-header-height);

  .menu {
    background-color: var(--app-background);
    border: none;
  }

  #logo-img {
    display: none;
  }
}


@media (min-width: 500px) {
  .header-container{

    #logo-img {
      display: block;
    }
  }
}
</style>