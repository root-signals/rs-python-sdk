// Main exports
export { RootSignals } from './client.js';

// Types
export type {
  ClientConfig,
  PaginatedResponse,
  ListParams,
  ExecutionPayload,
} from './types/common.js';
export { RootSignalsError } from './types/common.js';

// Resources
export type {
  EvaluatorListItem,
  EvaluatorDetail,
  ExecutionResult,
  EvaluatorListParams,
} from './resources/evaluators.js';

export type {
  Judge,
  JudgeDetail,
  JudgeExecutionResult,
  CreateJudgeData,
  UpdateJudgeData,
  JudgeExecutionPayload,
  JudgeListParams,
} from './resources/judges.js';

export type {
  ObjectiveList,
  ObjectiveDetail,
  CreateObjectiveData,
  UpdateObjectiveData,
  ObjectiveListParams,
} from './resources/objectives.js';

export type {
  ModelList,
  ModelDetail,
  CreateModelData,
  UpdateModelData,
  ModelListParams,
} from './resources/models.js';

export type {
  ExecutionLogList,
  ExecutionLogDetails,
  ExecutionLogListParams,
} from './resources/execution-logs.js';

// Additional resources
export { DatasetsResource } from './resources/datasets.js';

// Generated types (re-export for advanced usage)
export type { paths, components } from './generated/types.js';
