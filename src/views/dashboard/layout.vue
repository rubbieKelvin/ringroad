<template>
  <div class="h-full flex">
    <!-- side (move to other componenet) -->
    <div
      class="w-[24rem] border-r-slate-300 border-r-2 py-5 flex flex-col gap-2"
    >
      <!-- banner -->
      <div class="pb-2 px-5">
        <h1 class="text-2xl font-medium">Grus. IM</h1>
        <p class="text-xs text-gray-700">stuffsbyrubbie</p>
      </div>

      <!-- store profile -->
      <div
        class="flex gap-2 border border-slate-300 mx-5 p-2 rounded-md items-center"
      >
        <!-- logo -->
        <div
          class="w-12 h-12 flex items-center justify-center bg-gray-100 rounded-md"
        >
          <IconBuildingStore :size="28" />
        </div>

        <!-- name -->
        <div class="flex-grow">
          <p class="font-medium text-lg">Rubbie's store</p>
          <p class="uppercase text-sm">admin</p>
        </div>

        <!-- expand icon -->
        <button class="px-2">
          <IconChevronUp :size="21" />
        </button>
      </div>

      <!-- menu -->
      <div class="px-5 mt-2 flex flex-col gap-1 flex-grow">
        <NavigationMenuItem
          v-for="item in menu"
          :text="item.label"
          :icon="item.icon"
          :link="item.link"
          :badge="item.badge"
        />
      </div>

      <!-- user -->
      <div class="px-5 flex gap-2 items-center">
        <!-- profile -->
        <img
          src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.9E019Lxurmewapj7GTtvWgHaLH%26pid%3DApi&f=1&ipt=3eac40b8b353751ab0f7cace58f8d35fe4ab221ac235adfe31b4105dd55c2791&ipo=images"
          class="w-12 h-12 object-cover rounded-full"
        />

        <div class="flex-grow">
          <p class="text-lg">Rubbie kelvin</p>
          <p class="text-sm">dev.rubbie@gmail.com</p>
        </div>

        <!-- more menu -->
        <button>
          <IconDots :size="24" />
        </button>
      </div>
    </div>
    <!-- <p>Dashboard</p>
      <div class="flex gap-3">
        <RouterLink to="#" v-for="i in links" :key="i">
          {{ i }}
        </RouterLink>
      </div> -->

    <!-- body -->
    <div class="flex-grow">
      <RouterView class="h-full" />
    </div>
  </div>
</template>

<script lang="ts" setup>
import NavigationMenuItem from "@/components/NavigationMenuItem.vue";
import { FunctionalComponent } from "vue";
import {
  IconReportAnalytics,
  IconBuildingStore,
  IconChevronUp,
  IconDots,
} from "@tabler/icons-vue";
import { IconShoppingBag } from "@tabler/icons-vue";
import { IconTransactionDollar } from "@tabler/icons-vue";
import { useRoute } from "vue-router";
import { IconUsers } from "@tabler/icons-vue";
import { IconUserStar } from "@tabler/icons-vue";

const route = useRoute();
const { id } = route.params;

const menu: Array<{
  label: string;
  icon: FunctionalComponent;
  badge?: string;
  link: string | { name: string; params?: any };
}> = [
  {
    label: "Overview",
    icon: IconReportAnalytics,
    link: { name: "dashboard-home", params: { id } },
  },
  {
    label: "Inventory",
    icon: IconShoppingBag,
    link: { name: "dashboard-products", params: { id } },
    badge: "34",
  },
  {
    label: "Customers",
    icon: IconUsers,
    link: { name: "dashboard-customers", params: { id } },
    badge: "99+",
  },
  {
    label: "Members",
    icon: IconUserStar,
    link: { name: "dashboard-customers", params: { id } },
    badge: "3",
  },
  {
    label: "Transactions",
    icon: IconTransactionDollar,
    link: { name: "dashboard-transactions", params: { id } },
  },
];
</script>
