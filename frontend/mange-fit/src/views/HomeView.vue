<script setup lang="ts">
import HomeSaladComponent from '@/components/HomeSaladComponent.vue';
</script>

<template>
  <div class="background-circle"></div>
  <main class="home-container w-full flex">
    <section class="home-title-section text-center flex flex-column align-items-center  up-element">
      <p><span>Peça sua salada</span> na comodidade do seu lar</p>
      <button class="custom-button-light order">
        <RouterLink to="/order">Pedir já</RouterLink>
      </button>
    </section>

    <section class="home-image-section">
      <HomeSaladComponent />

    </section>
  </main>
</template>


<style scoped lang="scss">
.home-container {
  max-height: calc(100vh - var(--app-header-height));
  height: calc(100vh - var(--app-header-height));

  display: flex;
  flex-direction: column;

  .home-title-section {
    width: 100%;
    height: 30%;
    color: rgb(216, 208, 208);

    p {
      font-size: 1.8rem;

      span {
        font-weight: bold;
      }
    }
  }

  .home-image-section {
    width: 100%;
    height: 70%;
  }
}


@media (min-width: 500px) {
  .home-container {
    flex-direction: row;

    .home-title-section {
      width: 50%;
      height: 100%;
      justify-content: center;
      color: black;

      p {
        padding: 0.2rem;
        font-size: 2.8rem;

        span {
          font-weight: bold;
        }
      }

      .order {
        width: 12rem;
        height: 3rem;
      }
    }

    .home-image-section {
      width: 50%;
      height: 100%;
    }
  }
}
</style>