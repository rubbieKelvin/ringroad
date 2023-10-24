<template>
  <div>
    <p>Dashboard</p>
    <div class="flex gap-3">
      <RouterLink to="#" v-for="i in links" :key="i">
        {{ i }}
      </RouterLink>
    </div>
    <RouterView />
  </div>
</template>

<script lang="ts" setup>
const links = [
  "Home",
  "Items",
  "Suppliers",
  "Manage categories",
  "Staffs",
  "Settings",
];
</script>
