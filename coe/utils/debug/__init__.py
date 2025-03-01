# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
import torch.distributed as dist
import logging
import wandb


def get_gpu_memory_usage(rank: int = 0):
    if (not dist.is_initialized()) or (rank is None) or (dist.get_rank() == rank):
        memory_allocated = torch.cuda.memory_allocated() / 1024**3
        memory_reserved = torch.cuda.memory_reserved() / 1024**3

        message = f'{head}, memory allocated (GB): {memory_allocated}, memory reserved (GB): {memory_reserved}'

        if logger is None:
            print(message)
        else:
            logger.log(msg=message, level=level)
        

        # Convert to more readable units (GB)
        
        # Log to wandb
        try:
            wandb.log({
                "gpu/memory_allocated_gb": memory_allocated,
                "gpu/memory_reserved_gb": memory_reserved,  # This tracks reserved memory
            },
            step=None)  # Log to the current step
        except:
            pass # Ignore if wandb is not initialized