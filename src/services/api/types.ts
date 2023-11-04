interface JsonBodyHeader {
  "Content-Type": string;
}

interface AuthenticationHeader {
  Authorization: string;
}

export interface EndpointInterface {
  "[PO] /api/auth/signup": {
    data: {
      first_name: string;
      last_name: string;
      email: string;
      password: string;
    };
    header: JsonBodyHeader & AuthenticationHeader;
    response: {};
    path_args?: {};
  };
}
