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
  options: {
    data: EndpointInterface[T]["data"];
    path_args: EndpointInterface[T]["path_args"];
    authenticated?: boolean;
  }
) => {
  const [short_method, template_url] = endpoint.split(" ");

  const method = method_map[short_method];
  const url = options?.path_args
    ? use_template(template_url, options.path_args)
    : template_url;

  let token: string | null = null;

  if (options.authenticated) {
    token = localStorage.getItem("authtoken");
  }

  return await axios.request<EndpointInterface[T]["response"]>({
    url: BACKEND_BASE_URL + url,
    method,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    data: options.data,
  });
};
