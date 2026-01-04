class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7

        # OPTIMIZE IDEA 2:
        # Không cần phải tạo dictionary mà có thể loop lùi ngay từ list (eff, spd)
        
        eff_spd_li = [(eff, spd) for eff, spd in zip(efficiency, speed)]
        eff_spd_li.sort(reverse = True)

        best_spds = [] # -> [spd1, sp2, ...]
        sum_sdps = 0
        ans = 0

        for eff, spd in eff_spd_li:
            if len(best_spds) == k and best_spds[0] < spd:
                pop_spd = heapq.heappop(best_spds)
                sum_sdps -= pop_spd
            if len(best_spds) < k:
                heapq.heappush(best_spds, spd)
                sum_sdps += spd
                
            ans = max(ans, eff * sum_sdps)

        return ans % MOD
        
        # ----------------

        # IDEA 2:
        # Câu hỏi: Làm sao để tìm max sum của best k - 1 speed theo efficiency đó

        # Sort eff reverse rồi check từ thằng to nhất
        # mỗi lẫn giảm eff, kick speed bé nhất nếu length == k
        # nếu eff đó có > 1 speed, loop qua đám speed đó để lấy k thằng to nhất

        eff_spd_di = defaultdict(list)
        for eff, spd in zip(efficiency, speed):
            eff_spd_di[eff].append(spd)
        
        eff_spd_li = [(eff, sorted(spds)) for eff, spds in eff_spd_di.items()]
        eff_spd_li.sort(reverse = True)

        best_spds = [] # -> [spd1, sp2, ...]
        sum_sdps = 0
        ans = 0

        for eff, spds in eff_spd_li:
            for spd in spds:
                if len(best_spds) == k and best_spds[0] < spd:
                    pop_spd = heapq.heappop(best_spds)
                    sum_sdps -= pop_spd
                if len(best_spds) < k:
                    heapq.heappush(best_spds, spd)
                    sum_sdps += spd
                
            ans = max(ans, eff * sum_sdps)

        return ans % MOD


        # ----------------

        # IDEA 1: -> TLE
        # với mỗi cặp (a, b), kết hợp với tối đa k-1 số khác sao cho 
        # k-1 số khác có eff > b

        ans = 0
        
        for curr_sp, curr_ef in zip(speed, efficiency):
            avail = [(sp, ef) for sp, ef in zip(speed, efficiency) if ef >= curr_ef]
            avail.sort(reverse = True)
            best_sum = 0
            for i in range(min(k, len(avail))):
                best_sum = (best_sum + avail[i][0])

            ans = max(ans, (best_sum * curr_ef) ) 

        return ans % MOD


