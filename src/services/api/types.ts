interface Operation<D, R, A, P extends Record<string, string> | undefined> {
  data: D;
  response: R;
  args: A;
  params: Partial<P>;
}

export interface EndpointInterface {
  "[PO] /auth/exchange": Operation<
    { code: string },
    { token: string },
    undefined,
    undefined
  >;
}
