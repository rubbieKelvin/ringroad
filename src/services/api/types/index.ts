import { User } from "./models";
type I = Record<string, string> | null;

interface Operation<
  Input extends I,
  Output extends any | null,
  Args extends I,
  Params extends I
> {
  data: Input;
  response: Output;
  args: Args;
  params: Partial<Params>;
}

export interface EndpointInterface {
  // exchange code for token
  "[PO] /auth/exchange": Operation<
    { code: string },
    { token: string },
    null,
    null
  >;

  // get the current user
  "[GE] /api/user/me": Operation<null, User, null, null>;
  
  // create items
  // update item
  // list items
  // delete one item
  // delete multiple items
  // list the store for that user
  // create the store
  // delete store
  // update store
}
