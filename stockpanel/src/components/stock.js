import lodash from 'lodash'

var stock = {
  computeData (local) {
    for (let i = 0; i < local.length; i++) {
      let cur = local[i]
      // console.log('cur: ', cur)
      cur['expected_price'] = this.getPriceFromDividendAverage(cur['dividend'])
      cur['average_dividend'] = this.getAverageDividend(cur['dividend'])
      cur['distribution_yield'] = this.getDistributionYield(cur['dividend'], cur['yeps'])
      cur['average_distribution_yield'] = this.getAverageDistributionYield(cur['distribution_yield'])
      local[i] = cur
    }
    return local
  },
  getAverageDividend (dividend) {
    if (typeof dividend === 'undefined' || lodash.isEmpty(dividend)) {
      return 0
    }

    let total = 0
    for (var key in dividend) {
      const value = dividend[key]
      // console.log('cur key: ', key, ' value: ', value, " value.cash: ", value.cash)
      total += value.cash
    }

    return total / lodash.size(dividend)
  },
  getPriceFromDividendAverage (dividend) {
    return this.getAverageDividend(dividend) / 0.05
  },
  getDistributionYield (dividend, yeps) {
    let result = {}
    if (typeof dividend === 'undefined' || lodash.isEmpty(dividend)) {
      return result
    }
    if (typeof yeps === 'undefined' || lodash.isEmpty(yeps)) {
      return result
    }
    for (let year in dividend) {
      const d = dividend[year].cash
      const e = yeps[year]
      // result[year] = (d / e).toFixed(3)
      result[year] = d / e
    }
    return result
  },
  getAverageDistributionYield (distributionYield) {
    if (typeof distributionYield === 'undefined' || lodash.isEmpty(distributionYield)) {
      return 0
    }

    let total = 0
    // console.log(distributionYield)
    for (let year in distributionYield) {
      total += distributionYield[year]
      // console.log(total)
    }
    return total / lodash.size(distributionYield)
  }
}

export default stock
