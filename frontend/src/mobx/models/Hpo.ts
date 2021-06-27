import { types } from 'mobx-state-tree';

export const Hpo = types.model({
  id: types.identifierNumber,
  name: types.string,
  hpoId: types.string,
});
