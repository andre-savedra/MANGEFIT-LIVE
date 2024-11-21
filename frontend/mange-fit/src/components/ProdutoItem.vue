<script setup lang="ts">

// type propType = {
//   produto: Produto;
// };


// const props = defineProps<propType>();

// const emit = defineEmits(['eventoAdicionado']); 


</script>

<template>
  <section class="cartao flex flex-column align-items-center justify-content-center">
    <div class="check text-right">
      <Checkbox :binary="true" :readonly="true" />
    </div>
    <div class="produto-imagem">
      <img src="/salad1.jpg" />
    </div>
    <div>
      <h4 class="produto-nome">Salada Caesar </h4>
    </div>
    <div class="flex flex-row">
      <span>R$35</span>      
    </div>
    <div class="flex flex-row description">
      <span>Inspirada na costa italiana, uma explosão de sabores mediterrâneos!</span>      
    </div>
    <button disabled="!props.produto.quantidade" @click="" class="botao-add"
      label="props.produto.quantidade? 'Adicionar' : 'Não disponível'" />
  </section>
</template>

<style scoped lang="scss">
.cartao {
  width: 250px;
  max-width: 250px;
  height: auto;
  min-height: 250px;
  background-color: var(--app-dark-background);
  background-image: url("https://www.transparenttextures.com/patterns/45-degree-fabric-light.png");
  border-radius: 1.5rem;
  margin: 0.25rem;
  cursor: pointer;

  font-size: 1.0rem;
  color: white;

  &:hover {
    transform: scale(1.1);
    transition: 2s;
  }

  .produto-imagem {
    width: 90%;
    height: 55%;
    

    img {
      width: 100%;
      height: 100%;
    }
  }

  .produto-nome {
    margin: 0.5rem;    
  }
  .description span{
      font-size: 1.0rem;
    }

  .botao-add {
    width: 80%;
    height: 2rem;
    margin: 1rem;
  }

  .check {
    width: 95%;
  }
}

@media (min-width: 500px) {

  .cartao {
    width: 300px;
    max-width: 300px;
    height: auto;
    min-height: 350px;
    margin: 1.5rem;
    font-size: 1.5rem;

    .produto-imagem {
      max-width: 200px;
      max-height: 230px;

      img {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
