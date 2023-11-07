import { useApi } from "@/services/api";
import { User } from "@/services/api/types/models";
import { defineStore } from "pinia";
import { Ref, ref } from "vue";

export const useUserStore = defineStore("user", () => {
  const user: Ref<User | null> = ref(null);

  async function getUser() {
    if (user.value) return user.value;

    const { data } = await useApi(
      "[GE] /api/user/me",
      {
        data: null,
        args: null,
        params: null,
      },
      true
    );

    user.value = data;
    return data;
  }

  return {
    user,
    getUser,
  };
});
