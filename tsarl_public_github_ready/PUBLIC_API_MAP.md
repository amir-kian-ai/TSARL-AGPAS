# Public API map

## benchmark_advanced.py
- function `_cuda_sync()`
- function `_call_train_step()`
- class `AdvancedBenchmark`
- function `plot_summary()`
- function `main()`

## benchmark_speed.py
- function `_read_json_if_exists()`
- function `_find_log_file()`
- function `_infer_batch_size()`
- function `_ensure_images_per_sec()`
- function `_summarize_speed()`
- function `main()`

## eval_robust.py
- function `parse_frac()`
- function `_safe_get_model()`
- function `_select_state_dict()`
- function `_needs_wrap()`
- function `_build_model()`
- function `local_pgd_attack()`
- function `eval_clean()`
- function `eval_pgd()`
- function `main()`

## eval_rtsarl.py
- function `build_model()`
- function `load_checkpoint_flex()`
- function `normalize_state_dict_keys()`
- function `safe_load_model()`
- function `margin()`
- function `clean_eval()`
- function `pgd_eval()`
- function `collect_subset()`
- function `autoattack_eval()`
- function `main()`

## eval_rtsarl_trades_improved.py
- function `build_model_from_rb()`
- function `load_checkpoint_flex()`
- function `normalize_state_dict_keys()`
- function `safe_load_model()`
- function `margin()`
- function `local_pgd_attack()`
- function `clean_eval()`
- function `pgd_eval()`
- function `collect_subset()`
- function `autoattack_eval()`
- function `main()`

## eval_uar_tsarl.py
- function `ensure_parent_dir()`
- function `load_checkpoint_flex()`
- function `normalize_norm_name()`
- function `margin()`
- function `clean_eval()`
- function `pgd_eval()`
- function `autoattack_eval()`
- function `parse_args()`
- function `main()`

## plot_results.py
- function `_read_csv()`
- function `_maybe_read_json()`
- function `_find_epoch_col()`
- function `_find_first()`
- function `_find_best_pgd_rob_col()`
- function `_infer_batch_size_from_run_dir()`
- function `_get_throughput_series()`
- function `_save_plot()`
- function `main()`

## prepare_imagenet_val.py
- function `_to_int()`
- function `_to_str()`

## test_minimal.py

## train_pgd.py
- function `eval_clean_acc()`
- function `save_ckpt()`
- function `train()`

## train_robust_tsarl.py
- function `parse_frac()`
- function `set_seed()`
- function `save_json()`
- function `_safe_get_model()`
- function `_make_agpas()`
- function `_schedule_linear()`
- function `_schedule_int()`
- function `local_pgd_attack()`
- function `generate_adv()`
- function `eval_clean()`
- function `eval_pgd()`
- function `main()`

## train_rtsarl.py
- function `seed_everything()`
- function `build_model()`
- function `load_checkpoint_flex()`
- function `normalize_state_dict_keys()`
- function `safe_load_model()`
- function `set_requires_grad()`
- function `margin()`
- function `label_smoothing_loss()`
- function `kd_kl_loss()`
- function `teacher_targets()`
- function `base_schedule()`
- function `rand_bbox()`
- function `cutmix()`
- function `evaluate_clean()`
- function `main()`

## train_rtsarl_trades.py
- function `seed_everything()`
- function `build_model()`
- function `load_checkpoint_flex()`
- function `normalize_state_dict_keys()`
- function `safe_load_model()`
- class `ModelEMA`
- function `set_requires_grad()`
- function `label_smoothing_loss()`
- function `kd_kl_loss()`
- function `trades_kl_loss()`
- function `clean_probs_detached()`
- function `base_schedule()`
- function `rand_bbox()`
- function `cutmix()`
- function `evaluate_clean()`
- function `main()`

## train_rtsarl_trades_improved.py
- function `seed_everything()`
- class `ModelEMA`
- function `set_requires_grad()`
- function `build_teacher_and_student()`
- function `make_agpas_config()`
- function `agpas_forward()`
- function `agpas_regularizers()`
- function `label_smoothing_loss()`
- function `kd_kl_loss()`
- function `trades_kl_loss()`
- function `gradient_alignment_loss()`
- function `base_schedule()`
- function `rand_bbox()`
- function `cutmix()`
- function `kl_refine_from_init()`
- function `evaluate_clean()`
- function `local_pgd_attack()`
- function `evaluate_pgd_subset()`
- function `main()`

## train_tsarl.py

## train_uar_tsarl.py
- function `set_requires_grad()`
- function `softplus_margin()`
- function `teacher_targets()`
- function `base_schedule()`
- function `hardness_schedule()`
- function `tr_radius_schedule()`
- function `activated_channel_descriptor()`
- function `load_checkpoint_flex()`
- class `ResNetFeatureAdapter`
- class `MultiScaleHeads`
- function `pool_scale_feature()`
- class `PrototypeBank`
- function `top_level_groups()`
- function `params_by_group()`
- function `_safe_norm()`
- function `compute_criticality()`
- function `update_criticality_ema()`
- function `select_trainable_groups()`
- function `zero_frozen_grads()`
- function `select_diverse_hard_attack()`
- function `main()`

## train_uar_tsarl_v2.py
- function `set_requires_grad()`
- function `softplus_margin()`
- function `teacher_targets()`
- function `clean_kd_loss()`
- function `base_schedule()`
- function `hardness_schedule()`
- function `activated_channel_descriptor()`
- function `load_checkpoint_flex()`
- class `ResNetFeatureAdapter`
- class `MultiScaleHeads`
- function `pool_scale_feature()`
- class `PrototypeBank`
- function `top_level_groups()`
- function `params_by_group()`
- function `compute_criticality()`
- function `update_criticality_ema()`
- function `select_trainable_groups()`
- function `zero_frozen_grads()`
- function `select_diverse_hard_attack()`
- function `main()`

## tsarl/__init__.py

## tsarl/accelerated_train.py
- function `save_json()`
- function `parse_frac()`
- function `_construct_cfg()`
- function `set_seed()`
- function `local_pgd_attack()`
- function `safe_pgd_adv()`
- function `eval_clean()`
- function `eval_pgd()`
- function `main()`

## tsarl/agpas.py
- class `AGPASConfig`
- class `DifferentiableQPLayer`
- class `FeatureNet`
- class `EfficientMaskNet`
- class `TemporalWeights`
- class `Corrector`
- class `OptimizedAGPAS`

## tsarl/agpas_optimized.py
- class `AGPASConfig`
- class `DifferentiableQPLayer`
- class `EfficientMaskNetwork`
- class `TemporalAttention`
- class `CorrectorNetwork`
- class `OptimizedAGPAS`

## tsarl/agpas_uar.py
- function `smooth_distance()`
- class `UARAGPASConfig`
- class `MaskNet`
- class `Encoder`
- class `DynamicsNet`
- class `UARAGPAS`

## tsarl/data.py
- class `DataConfig`
- function `get_dataset_stats()`
- function `_canon_dataset()`
- function `_maybe_strong_cifar100_aug()`
- function `_cifar_transforms()`
- function `_imagenet_transforms()`
- function `get_loaders()`

## tsarl/meters.py
- class `AvgMeter`
- class `Timer`

## tsarl/models.py
- function `get_model()`

## tsarl/normalize.py
- function `get_stats()`
- class `NormalizeLayer`
- class `NormalizedModel`
- function `wrap_model()`

## tsarl/pgd.py
- function `pgd_attack()`

## tsarl/projection.py
- class `LinfProjectSTE`
- function `project_lp()`

## tsarl/qplayer.py
- function `solve_delta_qp_linf()`
- function `solve_delta_qp_l2_then_project()`

## tsarl/results_analyzer.py
- class `ResultsAnalyzer`
- function `main()`

## tsarl/train_optimized.py
- class `TrainingConfig`
- class `UnifiedOptimizerTrainer`
