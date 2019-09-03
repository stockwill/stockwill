// See
// https://www.vuetable.com/guide/api-vs-data-mode.html#data-mode
// https://codesandbox.io/s/y0z80ooxk9?from-embed
// TODO: pagination
export default [
  {
    name: 'symbol',
    sortField: 'symbol',
    title: '股票ID'
  },
  {
    name: 'company_name',
    title: '股票名'
    // sortField: 'company_name'
  },
  {
    name: 'current_price',
    sortField: 'current_price',
    title: '市價'
  },
  {
    name: 'expected_price',
    sortField: 'expected_price',
    title: '5%5年股利反推',
    formatter: (value) => {
      return value.toFixed(3)
    }
  },
  {
    name: 'dividend',
    sortField: 'dividend',
    title: '股利(現金)'
  },
  {
    name: 'distribution_yield',
    sortField: 'distribution_yield',
    title: '配息率',
    formatter: (v) => {
      let result = {}
      for (let year in v) {
        result[year] = v[year].toFixed(3)
      }
      return result
    }
  },
  {
    name: 'average_distribution_yield',
    sortField: 'average_distribution_yield',
    title: '平均配息率',
    formatter: (v) => {
      return v.toFixed(3)
    }
  }
]
