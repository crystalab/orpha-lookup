import { Instance, types } from 'mobx-state-tree';
import { createContext, useContext } from 'react';
import { RepoStore } from './stores/Repo.store';
import { LookupStore } from './stores/Lookup.store';

export const RootStore = types.model({
  lookupStore: types.optional(LookupStore, {}),
  repoStore: types.optional(RepoStore, {}),
});

export type RootInstance = Instance<typeof RootStore>;
const RootStoreContext = createContext<null | RootInstance>(null);

export const Provider = RootStoreContext.Provider;
export function useMst(): RootInstance {
  return useContext(RootStoreContext) as RootInstance;
}
