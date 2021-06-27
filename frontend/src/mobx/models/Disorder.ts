import { Instance, types } from 'mobx-state-tree';
import { DisorderHpo } from './DisorderHpo';

export const Disorder = types.model({
  id: types.identifierNumber,
  orphaCode: types.number,
  name: types.string,
  expertLink: types.maybe(types.string),
  disorderType: types.maybe(types.string),
  disorderGroup: types.maybe(types.string),
  score: types.maybeNull(types.number),
  hpos: types.array(types.reference(DisorderHpo)),
}).views(self => ({
  sortedHpos(selectedHpoIds: any) {
    return self.hpos.slice().sort((hpoA, hpoB) => {
      return Number(hpoB.hpo.id in selectedHpoIds) - Number(hpoA.hpo.id in selectedHpoIds);
    });
  },
}));

export type DisorderInstance = Instance<typeof Disorder>;
