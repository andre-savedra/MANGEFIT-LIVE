<script setup lang="ts">
import { RouterView, useRoute } from 'vue-router'
import HeaderComponent from './components/HeaderComponent.vue';
import { computed, ref, onMounted } from 'vue';

</script>

<template>  
  <main class="app-main-container w-full" >   
    <!-- {{ useRoute().name }}  -->
    <HeaderComponent />
    
    <RouterView/>
  </main>
</template>

<style scoped lang="scss">
.app-main-container {
 
  
}

.app-main-container:has(.background-circle) {
  position: relative;
  overflow: hidden;
}

// .home{
//   position: relative;
//   overflow: hidden;
// }
// .not-home{
//   position: fixed;
//   .background-circle{
//     display: none;
//   }
// }

</style>
