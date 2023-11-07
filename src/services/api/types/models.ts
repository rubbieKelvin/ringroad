export interface User {
  id: string;
  email: string;
  full_name: string;
  first_name: string | null;
  last_name: string | null;
  date_created: string;
}

export interface Item {
  name: string;
  brand: string;
  category: string;
  store: Store;
  purchase_price: number;
  selling_price: number;
  quantity: number;
}

export interface Store {
  owner: User;
  name: string;
  description: string;
}
