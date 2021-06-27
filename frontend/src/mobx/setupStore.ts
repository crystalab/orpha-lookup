import { RootStore } from './Root.store';
import { Environment } from './Environment';

export const setupStore = () => {
  const env = new Environment(process.env.REACT_APP_API_URL || '/api');
  return RootStore.create({}, env);
};
