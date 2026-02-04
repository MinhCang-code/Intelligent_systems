import numpy as np

# Hàm tam giác (Triangular Membership Function)
def trimf(x, a, b, c):
    return np.maximum(
        np.minimum((x - a) / (b - a + 1e-6), (c - x) / (c - b + 1e-6)),
        0
    )

# =============================================================================
# MIỀN GIÁ TRỊ T_in VÀ AC
# =============================================================================
x_T = np.linspace(20, 35, 300)
x_AC = np.linspace(0, 100, 300)

# =============================================================================
# BƯỚC 1: FUZZIFICATION - Chuyển giá trị crisp T_in thành độ thuộc mờ
# =============================================================================
def fuzzify_T_in(T_in):
    """
    Fuzzify nhiệt độ đầu vào T_in thành các mức độ thuộc:
    - cold (Lạnh): 20-22-25
    - comfort (Dễ chịu): 24-26-28
    - hot (Nóng): 27-30-35
    """
    mu_cold = trimf(T_in, 20, 22, 25)
    mu_comfort = trimf(T_in, 24, 26, 28)
    mu_hot = trimf(T_in, 27, 30, 35)
    return {
        "cold": float(mu_cold),
        "comfort": float(mu_comfort),
        "hot": float(mu_hot)
    }

# =============================================================================
# BƯỚC 2: ÁP DỤNG LUẬT MỜ (Fuzzy Rules)
# =============================================================================
def fuzzy_rules(T_in):
    """
    Áp dụng bộ luật mờ đơn giản:
    - IF T_in is LẠNH    -> AC Thấp
    - IF T_in is DỄ CHỊU -> AC Vừa
    - IF T_in is NÓNG    -> AC Cao
    """
    mu = fuzzify_T_in(T_in)
    
    # LUẬT MỜ (ĐƠN GIẢN):
    ac_low_strength = mu["cold"]      # Lạnh -> AC Thấp
    ac_med_strength = mu["comfort"]   # Dễ chịu -> AC Vừa
    ac_high_strength = mu["hot"]      # Nóng -> AC Cao
    
    return {
        "low": ac_low_strength,
        "med": ac_med_strength,
        "high": ac_high_strength
    }

# =============================================================================
# BƯỚC 3: DEFUZZIFICATION - Chuyển đầu ra mờ thành giá trị crisp
# =============================================================================
def defuzzify_AC(T_in):
    """
    Thực hiện defuzzification bằng phương pháp trọng tâm (centroid).
    
    Pipeline: fuzzification -> áp luật -> aggregation -> defuzzification
    """
    rules = fuzzy_rules(T_in)
    
    # Tập mờ output cho AC:
    #   Thấp (LOW): 0-0-40
    #   Vừa (MED): 20-50-80
    #   Cao (HIGH): 60-100-100
    mu_ac_low = trimf(x_AC, 0, 0, 40)
    mu_ac_med = trimf(x_AC, 20, 50, 80)
    mu_ac_high = trimf(x_AC, 60, 100, 100)
    
    # Áp dụng min (AND) & max (aggregation)
    aggregated = np.zeros_like(x_AC)
    aggregated = np.maximum(aggregated,
                            np.minimum(rules["low"], mu_ac_low))
    aggregated = np.maximum(aggregated,
                            np.minimum(rules["med"], mu_ac_med))
    aggregated = np.maximum(aggregated,
                            np.minimum(rules["high"], mu_ac_high))
    
    # Defuzzify dùng trọng tâm (centroid)
    if aggregated.sum() == 0:
        ac_crisp = 0.0
    else:
        ac_crisp = float(np.sum(aggregated * x_AC) / np.sum(aggregated))
    
    return ac_crisp, aggregated

# =============================================================================
# BƯỚC 4: KIỂM TRA VỚI VÀI GIÁ TRỊ T_in
# =============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("BỘ ĐIỀU KHIỂN MỜ CHO CÔNG SUẤT AC")
    print("Pipeline: Fuzzification -> Fuzzy Rules -> Defuzzification")
    print("=" * 60)
    
    test_T = [22, 25, 29, 32]
    
    print("\n--- KẾT QUẢ VỚI LUẬT GỐC ---")
    print("Luật: LẠNH->AC Thấp | DỄ CHỊU->AC Vừa | NÓNG->AC Cao")
    print("-" * 60)
    
    for T in test_T:
        mu = fuzzify_T_in(T)
        ac, _ = defuzzify_AC(T)
        print(f"T_in = {T}°C -> AC fuzzy ~ {ac:.2f}%")
        print(f"   [Độ thuộc: Lạnh={mu['cold']:.2f}, Dễ chịu={mu['comfort']:.2f}, Nóng={mu['hot']:.2f}]")
    
    # ==========================================================================
    # THỬ NGHIỆM LUẬT MỚI
    # ==========================================================================
    print("\n" + "=" * 60)
    print("THỬ NGHIỆM: Luật tiết kiệm hơn")
    print("Luật mới: LẠNH->AC Thấp | DỄ CHỊU->AC Thấp | NÓNG->AC Cao")
    print("=" * 60)
    
    def fuzzy_rules_saving(T_in):
        """
        Luật mờ tiết kiệm hơn:
        - IF T_in is LẠNH    -> AC Thấp
        - IF T_in is DỄ CHỊU -> AC Thấp (thay vì Vừa)
        - IF T_in is NÓNG    -> AC Cao
        """
        mu = fuzzify_T_in(T_in)
        ac_low_strength = max(mu["cold"], mu["comfort"])  # Cả Lạnh và Dễ chịu -> AC Thấp
        ac_med_strength = 0  # Không dùng AC Vừa
        ac_high_strength = mu["hot"]
        return {
            "low": ac_low_strength,
            "med": ac_med_strength,
            "high": ac_high_strength
        }
    
    def defuzzify_AC_saving(T_in):
        rules = fuzzy_rules_saving(T_in)
        mu_ac_low = trimf(x_AC, 0, 0, 40)
        mu_ac_med = trimf(x_AC, 20, 50, 80)
        mu_ac_high = trimf(x_AC, 60, 100, 100)
        
        aggregated = np.zeros_like(x_AC)
        aggregated = np.maximum(aggregated, np.minimum(rules["low"], mu_ac_low))
        aggregated = np.maximum(aggregated, np.minimum(rules["med"], mu_ac_med))
        aggregated = np.maximum(aggregated, np.minimum(rules["high"], mu_ac_high))
        
        if aggregated.sum() == 0:
            ac_crisp = 0.0
        else:
            ac_crisp = float(np.sum(aggregated * x_AC) / np.sum(aggregated))
        return ac_crisp, aggregated
    
    for T in test_T:
        ac_original, _ = defuzzify_AC(T)
        ac_saving, _ = defuzzify_AC_saving(T)
        diff = ac_saving - ac_original
        print(f"T_in = {T}°C -> AC gốc: {ac_original:.2f}% | AC tiết kiệm: {ac_saving:.2f}% | Chênh lệch: {diff:+.2f}%")

