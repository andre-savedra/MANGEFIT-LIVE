<script setup lang="ts">
import ProdutoItem from '@/components/ProdutoItem.vue';

</script>

<template>
  <div class="background-wallpaper"></div>
  <main class="order-container w-full flex flex-column ">
    <section
      class="order-title-section w-full text-center flex flex-column align-items-center justify-content-center  up-element">
      <p><span>Peça sua salada</span> na comodidade do seu lar</p>
    </section>

    <section class="order-products ">
      <div class="grid align-items-start justify-content-center">
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
        <ProdutoItem class="col-3" />
      </div>
    </section>
  </main>
</template>


<style scoped lang="scss">
.order-container {
  background-color: var(--app-background);
  .order-title-section {

    p {
      font-size: 1.8rem;

      span {
        font-weight: bold;
      }
    }
  }

  .order-products {
    margin: 5rem 0.5rem;
  }
}

@media (min-width: 500px) {

  .order-container {
    .order-title-section {

      p {
        padding: 0.2rem;
        font-size: 2.8rem;

        span {
          font-weight: bold;
        }
      }
    }

    .order-products {
      margin: 10rem;
    }

  }

}
</style>