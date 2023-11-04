export interface EndpointInterface {
  "[PO] /api/auth/signup": {
    data: {
      first_name: string;
      last_name: string;
      email: string;
      password: string;
    };
    response: {};
    path_args?: {};
  };
  "[PO] /api/user/me": {
    data: {};
    response: {
      id: string;
      email: string;
    };
    path_args?: {};
  };
}
