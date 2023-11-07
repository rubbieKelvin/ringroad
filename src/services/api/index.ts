import axios from "axios";
import { EndpointInterface } from "./types";
import { BACKEND_BASE_URL } from "@/constants";

const method_map: Record<string, string> = {
  "[PO]": "post",
  "[GE]": "get",
  "[PA]": "patch",
  "[PU]": "put",
  "[DE]": "delete",
};

const use_template = (text: string, template: Record<string, string>) => {
  let res = text;

  Object.entries(template).forEach(([key, value]) => {
    res = res.replace(`<${key}>`, value);
  });

  return res;
};

export const useApi = async <T extends keyof EndpointInterface>(
  endpoint: T,
  options: Pick<EndpointInterface[T], 'data'|"args"|"params">,
  authenticated: boolean = false
) => {
  const [short_method, template_url] = endpoint.split(" ");

  const method = method_map[short_method];
  const url = new URL(
    BACKEND_BASE_URL +
      (options?.args ? use_template(template_url, options.args) : template_url)
  );

  if (options.params)
    Object.entries(options.params).forEach(([key, value]) => {
      url.searchParams.set(key, String(value));
    });

  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };

  if (authenticated) {
    const token = localStorage.getItem("authtoken");
    headers.Authorization = `Bearer ${token}`;
  }

  return await axios.request<EndpointInterface[T]["response"]>({
    url: url.toString(),
    method,
    headers,
    data: options.data,
  });
};
