<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HeaderComponent from './components/HeaderComponent.vue';

</script>

<template>
  <main class="w-full">
    <HeaderComponent/>
    <RouterView />
  </main>
</template>

<style scoped lang="scss">

</style>
