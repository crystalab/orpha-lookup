import { types } from 'mobx-state-tree';
import { Hpo } from './Hpo';

export const DisorderHpo = types.model({
  id: types.identifierNumber,
  frequency: types.string,
  hpo: types.reference(Hpo),
});
