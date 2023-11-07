import { Store, User } from "./models";
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

  // create store
  "[PO] /api/store/create": Operation<
    { name: string; description: string },
    Store,
    null,
    null
  >;

  "[PA] /api/store/update/<id>": Operation<
    {
      name?: string;
      description?: string;
    },
    Store,
    { id: string },
    null
  >;

  "[DE] /api/store/delete/<id>": Operation<null, null, { id: string }, null>;

  // update item
  // list items
  // delete one item
  // delete multiple items
  // list the store for that user
  // create the store
  // delete store
  // update store
}

// create store
// PO api/stores

// get user's stores
// GET api/stores

// get a store
// GE api/store/<store_id>

// update a store
// PA api/store/<store_id>

// delete a store
// DE api/store/<store_id>

// get store items
// GE api/store/<store_id>/items

// create store items
// PO api/store/<store_id>/items
