import axios from "axios";
import { EndpointInterface } from "./types";

const API_URL = import.meta.env.VITE_BACKEND_BASE_URL;

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
    headers: EndpointInterface[T]["header"];
    path_args: EndpointInterface[T]["path_args"];
  }
) => {
  const [short_method, template_url] = endpoint.split(" ");

  const method = method_map[short_method];
  const url = options?.path_args
    ? use_template(template_url, options.path_args)
    : template_url;

  const headers = options.headers as any;

  return await axios.request<EndpointInterface[T]["response"]>({
    url: API_URL + url,
    method,
    headers: { ...headers },
    data: options.data,
  });
};
