import { types } from 'mobx-state-tree';
import { Hpo } from '../models/Hpo';
import { normalize, schema } from 'normalizr';
import { Disorder } from '../models/Disorder';
import { DisorderHpo } from '../models/DisorderHpo';

const HpoSchema = new schema.Entity('hpos');
const DisorderHpoSchema = new schema.Entity('disorderHpos', {
  hpo: HpoSchema,
})
const DisorderSchema = new schema.Entity('disorders', {
  hpos: [DisorderHpoSchema],
});

export const RepoStore = types.model({
  hpos: types.optional(types.map(Hpo), {}),
  disorders: types.optional(types.map(Disorder), {}),
  disorderHpos: types.optional(types.map(DisorderHpo), {}),
}).actions(self => ({
  updateModels(models: any) {
    for (const key of Object.keys(models)) {
      // @ts-ignore
      const repo: any = self[key];

      for (const modelId of Object.keys(models[key])) {
        repo.put(models[key][modelId]);
      }
    }
  },

}))
  .actions(self => ({
  persistHpoResponse(values: any[]) {
    const { entities, result } = normalize(values, [HpoSchema]);
    self.updateModels(entities);
    return result;
  },
  persistDisordersResponse(values: any[]) {
    const { entities, result } = normalize(values, [DisorderSchema]);
    console.log(result);
    self.updateModels(entities);
    return result;
  },
}));
