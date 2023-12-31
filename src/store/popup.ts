import { Ref, ref } from "vue";
import { defineStore } from "pinia";

export const usePopupStore = defineStore("popup", () => {
  const currentlyOpened: Ref<number | string | null> = ref(null);

  function setOpened(value: number | string | null) {
    currentlyOpened.value = value;
  }

  return { currentlyOpened, setOpened };
});
