"""Related Data Merge using DFS with Graph"""

GRAPH_FULL = {
    'Grower': {
        'MpciPolicy': ('Grower_OID', 'MpciPolicy_GrowerOID')
    },
    'MpciPolicy': {
        'MpciCoverage': ('MpciPolicy_OID', 'MpciCoverage _MpciPolicyOID'),
        'SBI': ('MpciPolicy_0ID', 'SBI_MpciPolicyOID')
    },
    'MpciCoverage': {
        'MpciPremiumLine': ('MpciCoverage_OID', 'MpciPremiumLine_MpciCoverageOID'),
        'AgrComnodityLine': ('MpciCoverage_OID', 'AgrCommodityLine_MpciCoverageOID'),
        'AgrIncomeExpense': ('MpciCoverage_OID', 'AgrIncomeExpense_MpciCoverageOID')
    },
    'MpciPremiumLine': {
        'MciPawQuestions': ('MpciPremiumLine_MpciPAWQuestionOID', 'MpciPawQuestions_OID'),
        'APH': ('MpciPremiumLine_APHOID', 'APH_OID')
    },
    'MpciPawQuestions': {
        'MpciPaw': ('MpciPawQuestions_OID', 'MpciPaw_MpciPAWQuestionOID')
    },
    'APH': {
        'ProductionHistory': ('APH_OID', 'ProductionHistory_APHOID')
    },
    'AgrIncomeExpense': {
        'AgrIncomeExpenseHistory': ('AgrIncomeExpense_OID', 'AgrIncomeExpenseHistory_AgrIncomeExpense0ID')
    }
}


# def join_graph_tables(base_df_name, base_df, graph, dataframes, join_set=None):
def join_graph_tables(base_df_name, graph, join_set=None):
    """Recursively join the base_df with all the tables in the graph."""
    if join_set is None:
        join_set = set()

    if base_df_name not in graph:
        # return base_df
        return

    for target_df_name, (base_key, target_key) in graph[base_df_name].items():
        if (base_df_name, target_df_name) in join_set:
            continue

        print((base_df_name, target_df_name))
        join_set.add((base_df_name, target_df_name))
        # target_df = dataframes[target_df_name]
        # base_df = base_df.merge(target_df,
        #                 how=' left',
        #                 left_on=base_key, right_on=target_key, suffixes=('', f'_{target_df_name.lower()}'))

        # base_df = join_graph_tables(target_df_name, base_df, graph, dataframes, join_set)
        join_graph_tables(target_df_name, graph, join_set)

    # return base_df
    return


if __name__ == "__main__":
    join_graph_tables("Grower", GRAPH_FULL)
