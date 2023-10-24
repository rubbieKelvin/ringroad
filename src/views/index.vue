<template>
  <div class="flex items-center justify-center">
    <div class="border border-gray-300 flex rounded-md gap-4 flex-col p-4">
      <h1 class="font-medium text-2xl">Inventory manager</h1>
      <p>Manage your store's inventory</p>
      <div class="flex gap-2">
        <RouterLink :to="{ name: 'signup' }" class="btn bg-gray-500 text-white"
          >Sign Up</RouterLink
        >
        <RouterLink :to="{ name: 'signin' }" class="btn border border-gray-300">
          Sign In
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.btn {
  @apply rounded-md flex-grow py-2 text-center;
}
</style>
